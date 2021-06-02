float[] FL_thigh_shoulder = new float[3];
float[] FL_hip = new float[3];
float[] FL_thigh = new float[3];
float[] FL_calf = new float[3];
float[] FL_foot = new float[3];

float[] FR_thigh_shoulder = new float[3];
float[] FR_hip = new float[3];
float[] FR_thigh = new float[3];
float[] FR_calf = new float[3];
float[] FR_foot = new float[3];

float[] RL_thigh_shoulder = new float[3];
float[] RL_hip = new float[3];
float[] RL_thigh = new float[3];
float[] RL_calf = new float[3];
float[] RL_foot = new float[3];

float[] RR_thigh_shoulder = new float[3];
float[] RR_hip = new float[3];
float[] RR_thigh = new float[3];
float[] RR_calf = new float[3];
float[] RR_foot = new float[3];

float[] base = new float[3];
float[] trunk = new float[3];
float[] imu_link = new float[3];

float[] FL_thigh_shoulder_com = new float[3];
float[] FL_hip_com = new float[3];
float[] FL_thigh_com = new float[3];
float[] FL_calf_com = new float[3];
float[] FL_foot_com = new float[3];

float[] FR_thigh_shoulder_com = new float[3];
float[] FR_hip_com = new float[3];
float[] FR_thigh_com = new float[3];
float[] FR_calf_com = new float[3];
float[] FR_foot_com = new float[3];

float[] RL_thigh_shoulder_com = new float[3];
float[] RL_hip_com = new float[3];
float[] RL_thigh_com = new float[3];
float[] RL_calf_com = new float[3];
float[] RL_foot_com = new float[3];

float[] RR_thigh_shoulder_com = new float[3];
float[] RR_hip_com = new float[3];
float[] RR_thigh_com = new float[3];
float[] RR_calf_com = new float[3];
float[] RR_foot_com = new float[3];

float[] base_com = new float[3];
float[] trunk_com = new float[3];
float[] imu_link_com = new float[3];

boolean FL_fc;
boolean FR_fc;
boolean RL_fc;
boolean RR_fc;

boolean[] footContacts = {FL_fc, FR_fc, RL_fc, RR_fc};

float[] com = new float[3];

float[][] links_com = {
                       FL_hip_com, FL_thigh_com, FL_calf_com, FL_foot_com,
                       FR_hip_com, FR_thigh_com, FR_calf_com, FR_foot_com,
                       RL_hip_com, RL_thigh_com, RL_calf_com, RL_foot_com,
                       RR_hip_com, RR_thigh_com, RR_calf_com, RR_foot_com,
                       FL_thigh_shoulder_com, FR_thigh_shoulder_com,
                       RL_thigh_shoulder_com, RR_thigh_shoulder_com,
                       trunk_com, base_com, imu_link_com
                     };

  
float[][] FL = {FL_hip, FL_thigh, FL_calf, FL_foot};
float[][] FR = {FR_hip, FR_thigh, FR_calf, FR_foot};
float[][] RL = {RL_hip, RL_thigh, RL_calf, RL_foot};
float[][] RR = {RR_hip, RR_thigh, RR_calf, RR_foot};

float[][][] limbs = {FL, FR, RL, RR};

float[] link = new float[3];
float[] p_link = new float[3];
String limbPrefix = "";

float radius = 0.01;

float[] bodyTracing = {0, 0, 0};

//Graphics
int scaling = 950;
float yaw = 0;
float pitch = 0;
int jointTrasparency = 160;
int animationSpeed = 1;

//Controls
//UP, RIGHT, DOWN, LEFT -> camera control
//Z -> zoom IN
//X -> zoom out
//C -> toggle center of mass
//V -> toggle center of mass of the individual links
//O -> toggle origin
//J -> toggle joints
//T -> toggle text
//I -> toggle axis
//Y -> toggle tracing
//G -> increase units traced
//H -> decrease units traced
//U -> toggle full tracing
//Q -> increase animation speed
//A -> decrease decrease
//L -> toggle joints coloring

boolean drawCOM = true;
boolean drawLinksCOM = false;
boolean drawOrigin = true;
boolean drawJoints = true;
boolean drawText = true;
boolean drawAxis = false;
boolean drawTracing = false;
boolean fullTracing = false;
boolean pause = false;
boolean jointsColor = false;

int unitsTraced = 10;

int keyValue = 0;

int time = 0;

JSONArray timeline;

void setup() {
  size(1124, 800, P3D);
  stroke(255);
  strokeWeight(2);
  fill(255);
  textSize(25);
  sphereDetail(6);
  background(0);
  
  //loading JSON file
  timeline = loadJSONArray("datasets/data.json");
  
  frameRate(90);
}

void draw() {
  //Basic eviroment setup
  background(0);
  lights();
  translate(1024/2, 900/2, -200);
  
  if(time >= timeline.size()) {
    time = 850;
  }
  
  updateCamera();
  updateDataPoint(time);
  drawCOMs();
  drawSkeleton(255);
  skeletonTracing(unitsTraced);
  checkInputs();
  
  if(!pause && frameCount % animationSpeed == 0) {
    time++;
  }
  
  printLogs();
}
