import { medico } from "./medico.response";

export interface agenda {
  id: number;
  dia: string;
  horarios: string[];
  medico: medico;
}
