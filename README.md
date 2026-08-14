# 트레이딩 봇 랩 (Hugo Blog)

트레이딩 봇 개발기를 기록하는 개인 블로그. Hugo + PaperMod 테마.

## 로컬에서 미리보기

```bash
hugo server -D
```

브라우저에서 http://localhost:1313 접속.

## 새 글 쓰기

```bash
hugo new content posts/글-제목.md
```

`content/posts/` 폴더에 파일이 생성됩니다. `draft: true`를 `false`로 바꾸면 발행됩니다.

## 빌드 (배포용 정적 파일 생성)

```bash
hugo --minify
```

`public/` 폴더에 결과물이 생성됩니다. 이 폴더를 Netlify, Vercel, GitHub Pages, Cloudflare Pages 등에 올리면 됩니다.

## 폴더 구조

- `hugo.yaml` — 사이트 설정 (제목, 메뉴, 테마 옵션)
- `content/posts/` — 블로그 글
- `content/about.md` — 소개 페이지
- `themes/PaperMod/` — 테마 (git submodule)
- `archetypes/default.md` — 새 글 기본 템플릿

## 참고

- baseURL을 실제 배포 도메인으로 바꿔야 합니다 (`hugo.yaml` 맨 위).
- 테마 업데이트: `git submodule update --remote --merge`
- Hugo 버전: v0.165.0 extended (PaperMod가 v0.146.0 이상을 요구합니다)
