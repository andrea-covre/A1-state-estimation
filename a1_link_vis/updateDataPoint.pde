void updateDataPoint(int time) {
  JSONArray temp;
  JSONObject dataPoint = timeline.getJSONObject(time);
  
  //----------------- FL -------------------------------
  
  temp = dataPoint.getJSONArray("FL_thigh_shoulder");
  FL_thigh_shoulder[0] = temp.getFloat(0);
  FL_thigh_shoulder[1] = temp.getFloat(1);
  FL_thigh_shoulder[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_hip");
  FL_hip[0] = temp.getFloat(0);
  FL_hip[1] = temp.getFloat(1);
  FL_hip[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_thigh");
  FL_thigh[0] = temp.getFloat(0);
  FL_thigh[1] = temp.getFloat(1);
  FL_thigh[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_calf");
  FL_calf[0] = temp.getFloat(0);
  FL_calf[1] = temp.getFloat(1);
  FL_calf[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_foot");
  FL_foot[0] = temp.getFloat(0);
  FL_foot[1] = temp.getFloat(1);
  FL_foot[2] = temp.getFloat(2);
  
  //----------------- FR -------------------------------
  
  temp = dataPoint.getJSONArray("FR_thigh_shoulder");
  FR_thigh_shoulder[0] = temp.getFloat(0);
  FR_thigh_shoulder[1] = temp.getFloat(1);
  FR_thigh_shoulder[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_hip");
  FR_hip[0] = temp.getFloat(0);
  FR_hip[1] = temp.getFloat(1);
  FR_hip[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_thigh");
  FR_thigh[0] = temp.getFloat(0);
  FR_thigh[1] = temp.getFloat(1);
  FR_thigh[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_calf");
  FR_calf[0] = temp.getFloat(0);
  FR_calf[1] = temp.getFloat(1);
  FR_calf[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_foot");
  FR_foot[0] = temp.getFloat(0);
  FR_foot[1] = temp.getFloat(1);
  FR_foot[2] = temp.getFloat(2);
  
  //----------------- RL -------------------------------
  
  temp = dataPoint.getJSONArray("RL_thigh_shoulder");
  RL_thigh_shoulder[0] = temp.getFloat(0);
  RL_thigh_shoulder[1] = temp.getFloat(1);
  RL_thigh_shoulder[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_hip");
  RL_hip[0] = temp.getFloat(0);
  RL_hip[1] = temp.getFloat(1);
  RL_hip[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_thigh");
  RL_thigh[0] = temp.getFloat(0);
  RL_thigh[1] = temp.getFloat(1);
  RL_thigh[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_calf");
  RL_calf[0] = temp.getFloat(0);
  RL_calf[1] = temp.getFloat(1);
  RL_calf[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_foot");
  RL_foot[0] = temp.getFloat(0);
  RL_foot[1] = temp.getFloat(1);
  RL_foot[2] = temp.getFloat(2);
  
  //----------------- FR -------------------------------
  
  temp = dataPoint.getJSONArray("RR_thigh_shoulder");
  RR_thigh_shoulder[0] = temp.getFloat(0);
  RR_thigh_shoulder[1] = temp.getFloat(1);
  RR_thigh_shoulder[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_hip");
  RR_hip[0] = temp.getFloat(0);
  RR_hip[1] = temp.getFloat(1);
  RR_hip[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_thigh");
  RR_thigh[0] = temp.getFloat(0);
  RR_thigh[1] = temp.getFloat(1);
  RR_thigh[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_calf");
  RR_calf[0] = temp.getFloat(0);
  RR_calf[1] = temp.getFloat(1);
  RR_calf[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_foot");
  RR_foot[0] = temp.getFloat(0);
  RR_foot[1] = temp.getFloat(1);
  RR_foot[2] = temp.getFloat(2);
  
  //----------------- other links ------------------------
  
  temp = dataPoint.getJSONArray("trunk");
  trunk[0] = temp.getFloat(0);
  trunk[1] = temp.getFloat(1);
  trunk[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("base");
  base[0] = temp.getFloat(0);
  base[1] = temp.getFloat(1);
  base[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("imu_link");
  imu_link[0] = temp.getFloat(0);
  imu_link[1] = temp.getFloat(1);
  imu_link[2] = temp.getFloat(2);
  
  //----------------- FL_com -------------------------------
  
  temp = dataPoint.getJSONArray("FL_thigh_shoulder_com");
  FL_thigh_shoulder_com[0] = temp.getFloat(0);
  FL_thigh_shoulder_com[1] = temp.getFloat(1);
  FL_thigh_shoulder_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_hip_com");
  FL_hip_com[0] = temp.getFloat(0);
  FL_hip_com[1] = temp.getFloat(1);
  FL_hip_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_thigh_com");
  FL_thigh_com[0] = temp.getFloat(0);
  FL_thigh_com[1] = temp.getFloat(1);
  FL_thigh_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_calf_com");
  FL_calf_com[0] = temp.getFloat(0);
  FL_calf_com[1] = temp.getFloat(1);
  FL_calf_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FL_foot_com");
  FL_foot_com[0] = temp.getFloat(0);
  FL_foot_com[1] = temp.getFloat(1);
  FL_foot_com[2] = temp.getFloat(2);
  
  //----------------- FR_com -------------------------------
  
  temp = dataPoint.getJSONArray("FR_thigh_shoulder_com");
  FR_thigh_shoulder_com[0] = temp.getFloat(0);
  FR_thigh_shoulder_com[1] = temp.getFloat(1);
  FR_thigh_shoulder_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_hip_com");
  FR_hip_com[0] = temp.getFloat(0);
  FR_hip_com[1] = temp.getFloat(1);
  FR_hip_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_thigh_com");
  FR_thigh_com[0] = temp.getFloat(0);
  FR_thigh_com[1] = temp.getFloat(1);
  FR_thigh_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_calf_com");
  FR_calf_com[0] = temp.getFloat(0);
  FR_calf_com[1] = temp.getFloat(1);
  FR_calf_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("FR_foot_com");
  FR_foot_com[0] = temp.getFloat(0);
  FR_foot_com[1] = temp.getFloat(1);
  FR_foot_com[2] = temp.getFloat(2);
  
  //----------------- RL_com -------------------------------
  
  temp = dataPoint.getJSONArray("RL_thigh_shoulder_com");
  RL_thigh_shoulder_com[0] = temp.getFloat(0);
  RL_thigh_shoulder_com[1] = temp.getFloat(1);
  RL_thigh_shoulder_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_hip_com");
  RL_hip_com[0] = temp.getFloat(0);
  RL_hip_com[1] = temp.getFloat(1);
  RL_hip_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_thigh_com");
  RL_thigh_com[0] = temp.getFloat(0);
  RL_thigh_com[1] = temp.getFloat(1);
  RL_thigh_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_calf_com");
  RL_calf_com[0] = temp.getFloat(0);
  RL_calf_com[1] = temp.getFloat(1);
  RL_calf_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RL_foot_com");
  RL_foot_com[0] = temp.getFloat(0);
  RL_foot_com[1] = temp.getFloat(1);
  RL_foot_com[2] = temp.getFloat(2);
  
  //----------------- FR_com -------------------------------
  
  temp = dataPoint.getJSONArray("RR_thigh_shoulder_com");
  RR_thigh_shoulder_com[0] = temp.getFloat(0);
  RR_thigh_shoulder_com[1] = temp.getFloat(1);
  RR_thigh_shoulder_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_hip_com");
  RR_hip_com[0] = temp.getFloat(0);
  RR_hip_com[1] = temp.getFloat(1);
  RR_hip_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_thigh_com");
  RR_thigh_com[0] = temp.getFloat(0);
  RR_thigh_com[1] = temp.getFloat(1);
  RR_thigh_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_calf_com");
  RR_calf_com[0] = temp.getFloat(0);
  RR_calf_com[1] = temp.getFloat(1);
  RR_calf_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("RR_foot_com");
  RR_foot_com[0] = temp.getFloat(0);
  RR_foot_com[1] = temp.getFloat(1);
  RR_foot_com[2] = temp.getFloat(2);
  
  //----------------- other links_com ------------------------
  
  temp = dataPoint.getJSONArray("trunk_com");
  trunk_com[0] = temp.getFloat(0);
  trunk_com[1] = temp.getFloat(1);
  trunk_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("base_com");
  base_com[0] = temp.getFloat(0);
  base_com[1] = temp.getFloat(1);
  base_com[2] = temp.getFloat(2);
  
  temp = dataPoint.getJSONArray("imu_link_com");
  imu_link_com[0] = temp.getFloat(0);
  imu_link_com[1] = temp.getFloat(1);
  imu_link_com[2] = temp.getFloat(2);
  
  //----------------- COM --------------------------
  
  temp = dataPoint.getJSONArray("com");
  com[0] = temp.getFloat(0);
  com[1] = temp.getFloat(1);
  com[2] = temp.getFloat(2);
  
  //------------ Foot Contact ---------------------
  
  footContacts[0] = dataPoint.getBoolean("FL_fc");
  footContacts[1] = dataPoint.getBoolean("FR_fc");
  footContacts[2] = dataPoint.getBoolean("RL_fc");
  footContacts[3] = dataPoint.getBoolean("RR_fc");

}
