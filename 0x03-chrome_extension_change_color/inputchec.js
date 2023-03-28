// This is for image resizer VS Code extension
let widthXheight = "16*16"
let resizeDimensions

if (/\d+\s*x\s*\d+/.test(widthXheight)) {
  resizeDimensions = widthXheight.split("x");
  console.log("TRuuu")
}
else if (/\d+\s*\*\s*\d+/.test(widthXheight)) {
  console.log("step 1")

  console.log(widthXheight)

  widthXheight = widthXheight.replace(/\*/, "x")

  console.log("step 2")
  console.log(widthXheight)

  resizeDimensions = widthXheight.split("*");
  console.log("Flase")
}
console.log(resizeDimensions)
