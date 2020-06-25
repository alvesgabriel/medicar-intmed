import { medico } from "./medico.response";

export interface consulta {
  id: number,
  dia: string,
  horario: string,
  data_agendamento: string,
  medico: medico,
}