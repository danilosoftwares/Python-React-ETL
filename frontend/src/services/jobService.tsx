import { JobResponse } from '../types/jobs';
import api from './baseService';

export const fetchJob = async (id: string): Promise<JobResponse> => {
  const response = await api.get<JobResponse>(`/jobs/byId?job_id=${id}`);
  return response.data;
};
