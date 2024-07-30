let offset = 0;
let amp = 1;
let slider;


function setup() {
  createCanvas(400, 400);
  
  slider = createSlider(0.01, 5, 0.5); // min, max, start
  slider.position(0,400); // x and y
  slider.size(400, 20); // width and height
}


function draw() {
  //getting my pushes in
  background(220);
  stroke(4);
  noFill();
  beginShape();
  vertex(0, height);
  
  for(let x = 0; x < width; x++){
    let angle = offset + x * 0.05;
    
    //map y values from [-1,1] to [150,250]
    let y = map(sin(angle), -slider.value(), slider.value(), 150, 250);
    
    vertex(x,y);
  }
  endShape();
  offset += 0.1;
}