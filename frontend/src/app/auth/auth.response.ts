export interface AuthResponse {
  user: {
    id: number,
    name: string,
    token: string,
  };
}