const apiUrl = import.meta.env.VITE_API_URL;

export const api = {
  getPartners: () =>
    fetch(`${apiUrl}/partners/`).then((res) => res.json()),
};