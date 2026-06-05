export function drivePhotoUrl(url: string | null | undefined): string | null {
  if (!url) return null;
  const match = url.match(/[?&]id=([\w-]+)/);
  if (!match) return url;
  return `https://lh3.googleusercontent.com/d/${match[1]}`;
}
