void drawBase() {
  if(drawOrigin) {
    radius = 0.01 * scaling;
    fill(255, 0, 255, 200);
    sphere(radius);
  }
  if(drawAxis) {
    stroke(0, 255, 0, 100);
    line(0, 0, 1*scaling/2, 0, 0, -1*scaling/2);
    stroke(0, 0, 255, 100);
    line(0, 1*scaling/2, 0, 0, -1*scaling/2, 0);
    stroke(255, 0, 0, 100);
    line(1*scaling/2, 0, 0, -1*scaling/2, 0, 0);
  }
  fill(180, 180, 180, 30);
  stroke(255);
  box(0.267*scaling, 0.194*scaling, 0.114*scaling);
  fill(255);
}

void drawSkeleton(int trasparency) {
  stroke(255, 255, 255, trasparency);
  fill(255, 255, 255, trasparency);
  
  for (int i = 0; i < 4; i++) {
    
    switch(i) {
      case 0:
        limbPrefix = "FL";
        break;
        
      case 1:
        limbPrefix = "FR";
        break;
        
      case 2:
        limbPrefix = "RL";
        break;
        
      case 3:
        limbPrefix = "RR";
        break;
    }
    
    if (!(trasparency != 255 && fullTracing == false)) {
      
      if(footContacts[i]) {
        stroke(230, 15, 255);
      }
    
      link = limbs[i][0];
      if (trasparency == 255) {
        line(0, 0, 0, link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      }
      pushMatrix();
      translate(link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      fill(255, 255, 255, trasparency);
      if(drawJoints) {
        sphere(radius);
      }
      if(drawText  && trasparency == 255) {
        stroke(255);
        pushMatrix();
        rotateX(radians(-pitch));
        rotateY(radians(-yaw));
        text(limbPrefix + "_hip", 10, 30); 
        popMatrix();
      }
      popMatrix();
      
      if(footContacts[i]) {
        stroke(230, 15, 255);
      }
      
      p_link = link;
      link = limbs[i][1];
      line(p_link[0]*scaling, -p_link[1]*scaling, p_link[2]*scaling, link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      pushMatrix();
      translate(link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      stroke(255, 255, 255, trasparency);
      if(drawJoints) {
        if(jointsColor) {
          stroke(0, 0, 255, trasparency);
        }
        sphere(radius);
        stroke(255, 255, 255, trasparency);
      }
      if(drawText  && trasparency == 255) {
        stroke(255);
        pushMatrix();
        rotateX(radians(-pitch));
        rotateY(radians(-yaw));
        text(limbPrefix + "_thigh", 10, 30); 
        popMatrix();
      }
      popMatrix();
      
      if(footContacts[i]) {
        stroke(230, 15, 255);
      }
      
      p_link = link;
      link = limbs[i][2];
      line(p_link[0]*scaling, -p_link[1]*scaling, p_link[2]*scaling, link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      pushMatrix();
      translate(link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      stroke(255, 255, 255, trasparency);
      if(drawJoints) {
        if(jointsColor) {
          stroke(255, 0, 0, trasparency);
        }
        sphere(radius);
        stroke(255, 255, 255, trasparency);
      }
      if(drawText  && trasparency == 255) {
        stroke(255);
        pushMatrix();
        rotateX(radians(-pitch));
        rotateY(radians(-yaw));
        text(limbPrefix + "_calf", 10, 30); 
        popMatrix();
      }
      popMatrix();
    }
    
    if(footContacts[i]) {
        stroke(230, 15, 255);
      }
    
    p_link = link;
    link = limbs[i][3];
    if (!(trasparency != 255 && fullTracing == false)) {
      line(p_link[0]*scaling, -p_link[1]*scaling, p_link[2]*scaling, link[0]*scaling, -link[1]*scaling, link[2]*scaling);
    }
    pushMatrix();
    translate(link[0]*scaling, -link[1]*scaling, link[2]*scaling);
    stroke(255, 255, 255, trasparency);
    if(drawJoints) {
      if(jointsColor) {
        stroke(0, 255, 0, trasparency);
      }
      sphere(radius);
      stroke(255, 255, 255, trasparency);
    }
    if(drawText  && trasparency == 255) {
      stroke(255);
      pushMatrix();
      rotateX(radians(-pitch));
      rotateY(radians(-yaw));
      text(limbPrefix + "_foot", 10, 30); 
      popMatrix();
    }
    popMatrix();
  }
}
