void checkInputs()  {
  if(keyPressed) {
    int change = 1;
    if (keyCode == LEFT) {
      yaw -= change;
    }
    if (keyCode == RIGHT) {
      yaw += change;
    }
    if (keyCode == UP) {
      pitch += change;
    }
    if (keyCode == DOWN) {
      pitch -= change;
    }
    if (key == 'z') {
      scaling += change;
    }
    if (key == 'x') {
      scaling -= change;
    }
    if (key == 'g') {
      if (unitsTraced < timeline.size()*0.18) {
        unitsTraced += 1;
      }
    }
    if (key == 'h') {
      if (unitsTraced > 0) {
        unitsTraced -= 1;
      }
    }
  }
}

void keyPressed() {
  if (key == 'o') {
    drawOrigin = !drawOrigin;
  }
  if (key == 'c') {
    drawCOM = !drawCOM;
  }
  if (key == 'v') {
    drawLinksCOM = !drawLinksCOM;
  }
  if (key == 'j') {
    drawJoints = !drawJoints;
  }
  if (key == 't') {
    drawText = !drawText;
  }
  if (key == 'i') {
    drawAxis = !drawAxis;
  }
  if (key == 'y') {
    drawTracing = !drawTracing;
  }
  if (key == 'u') {
    fullTracing = !fullTracing;
  }
  if (key == 'p') {
    pause = !pause;
  }
  if (key == 'q') {
      if (animationSpeed > 1) {
        animationSpeed -= 1;
      }
    }
    if (key == 'a') {
      if (animationSpeed < 100) {
        animationSpeed += 1;
      }
    }
    if (key == 'l') {
      jointsColor = !jointsColor;
    }
}
