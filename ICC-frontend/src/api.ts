const apiUrl = import.meta.env.VITE_API_URL;

export const api = {
  getMembers: () =>
    fetch(`${apiUrl}/members/`).then((res) => res.json()),

  getMember: (id: number) =>
    fetch(`${apiUrl}/members/${id}/`).then((res) => res.json()),

  getPartners: () =>
    fetch(`${apiUrl}/partners/`).then((res) => res.json()),

  getPartner: (id: number) =>
    fetch(`${apiUrl}/partners/${id}/`).then((res) => res.json()),

  getProjects: () =>
    fetch(`${apiUrl}/projects/`).then((res) => res.json()),

  getProject: (id: number) =>
    fetch(`${apiUrl}/projects/${id}/`).then((res) => res.json()),

  getStatistics: () =>
    fetch(`${apiUrl}/statistics/`).then((res) => res.json()),
};
