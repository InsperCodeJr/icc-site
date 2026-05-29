export function drivePhotoUrl(url: string | null | undefined): string | null {
  if (!url) return null;
  const match = url.match(/[?&]id=([\w-]+)/);
  if (!match) return url;
  return `https://drive.google.com/thumbnail?id=${match[1]}&sz=w400`;
}
