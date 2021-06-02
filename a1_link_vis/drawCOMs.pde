void drawCOMs() {
  //draw total COM
  if(drawCOM) {
    fill(0, 255, 0);
    pushMatrix();
    translate(com[0]*scaling, -com[1]*scaling, com[2]*scaling);
    sphere(radius);
    popMatrix();
    fill(255);
  }
  
  /*
  pushMatrix();
  translate(bodyTracing[0], bodyTracing[1], bodyTracing[2]);
  bodyTracing[0] -= 0.5;
  //bodyTracing[1] += 1;
  //bodyTracing[2] += 1;
  sphere(5);
  popMatrix();
  */
  
  drawBase();
  
  //draw individual COMs
  if(drawLinksCOM) {
    //Limbs COMs
    for (float[] link : links_com) {
      pushMatrix();
      stroke(0, 0, 255);
      translate(link[0]*scaling, -link[1]*scaling, link[2]*scaling);
      sphere(radius * 0.75);
      popMatrix();
    }
  }
}
