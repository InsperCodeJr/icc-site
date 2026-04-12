const BASE_URL = "http://127.0.0.1:8000/api";

export const api = {
  getMembers: () =>
    fetch(`${BASE_URL}/members/`).then((res) => res.json()),

  getMember: (id: number) =>
    fetch(`${BASE_URL}/members/${id}/`).then((res) => res.json()),

  getPartners: () =>
    fetch(`${BASE_URL}/partners/`).then((res) => res.json()),

  getPartner: (id: number) =>
    fetch(`${BASE_URL}/partners/${id}/`).then((res) => res.json()),

  getProjects: () =>
    fetch(`${BASE_URL}/projects/`).then((res) => res.json()),

  getProject: (id: number) =>
    fetch(`${BASE_URL}/projects/${id}/`).then((res) => res.json()),

  getStatistics: () =>
    fetch(`${BASE_URL}/statistics/`).then((res) => res.json()),
};
