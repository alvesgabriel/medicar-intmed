import { especialidade } from "./especialidade.response";

export interface medico {
  id: number,
  crm: number,
  nome: string,
  especialidade: especialidade
}