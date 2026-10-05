const API_BASE_URL = "http://127.0.0.1:8000";

export async function getIssues() {
  const response = await fetch(`${API_BASE_URL}/api/issues/`);

  if (!response.ok) {
    throw new Error("Failed to fetch issues");
  }

  return response.json();
}