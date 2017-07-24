function initializeGallery()
{
  var imgs,i;
  imgs = document.getElementsByClassName("preview-frame");
  for(i=0;i<imgs.length;i++)
  {
    imgs[i].onmouseover=function(){showTooltip(this);};
    imgs[i].onmouseout=function(){hideTooltip(this);};
  }
}

function showTooltip(x) {
  document.getElementById("tooltip-title").innerHTML = x.dataset.title;
  document.getElementById("tooltip-date").innerHTML = x.dataset.date;
  document.getElementById("tooltip-frame").style.display = "block";
  document.addEventListener('mousemove', moveTooltip, false);
}

function hideTooltip(x) {
  document.getElementById("tooltip-frame").style.display = "none";
  document.removeEventListener('mousemove', moveTooltip, false);
}

function moveTooltip(e) {
  tooltipFrame = document.getElementById("tooltip-frame")
  tooltipFrame.style.left = e.pageX + 10 + 'px';
  tooltipFrame.style.top = e.pageY + 20 + 'px';  
}


window.onload=function(){
  initializeGallery();
}



