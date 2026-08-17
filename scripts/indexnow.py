"""배포 후 최근 갱신된 URL을 IndexNow(빙·네이버)에 통보한다."""
import datetime
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET

HOST = "botlab.co.kr"
KEY = "731b551d537148ab911452b972486a39"
WINDOW_DAYS = 2
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def recent_urls():
    raw = urllib.request.urlopen("https://" + HOST + "/sitemap.xml", timeout=30).read()
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=WINDOW_DAYS)
    picked = []
    for node in ET.fromstring(raw).findall("s:url", NS):
        loc = node.findtext("s:loc", namespaces=NS)
        if not loc:
            continue
        lastmod = node.findtext("s:lastmod", namespaces=NS)
        if lastmod:
            try:
                stamp = datetime.datetime.fromisoformat(lastmod)
            except ValueError:
                stamp = None
            if stamp is not None:
                if stamp.tzinfo is None:
                    stamp = stamp.replace(tzinfo=datetime.timezone.utc)
                if stamp < cutoff:
                    continue
        picked.append(loc)
    return picked[:100]


def main():
    try:
        urls = recent_urls()
    except Exception as err:
        print("sitemap read failed: " + str(err))
        return 0
    if not urls:
        print("no recently updated urls; skipping")
        return 0
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": "https://" + HOST + "/" + KEY + ".txt",
        "urlList": urls,
    }).encode("utf-8")
    request = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as res:
            print("IndexNow " + str(res.status) + " / " + str(len(urls)) + " urls")
    except Exception as err:
        print("IndexNow submit failed: " + str(err))
    return 0


if __name__ == "__main__":
    sys.exit(main())
