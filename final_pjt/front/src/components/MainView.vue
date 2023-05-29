<template>
  <div id="main" @click="onClickChange">
    <span style="color:white; top:25%; left: 25%; z-index:999; background: none;">클릭 후 5초만 기다려주세요.</span>
  </div>
</template>

<script>
import * as PIXI from 'pixi.js';

import star from '@/assets/star.png'

export default{
  name: "MainView",
  data(){
    return{
      app : new PIXI.Application({resizeTo: window}),
      // Get the texture for star.
      starTexture : PIXI.Texture.from(star),
      starAmount : 1000,
      cameraZ : 0,
      fov : 20,
      baseSpeed : 0.025,
      speed : 0,
      warpSpeed : 0,
      starStretch : 5,
      starBaseSize : 0.05,
      stars: [],
      TimerOn: false
    }
  },
  methods: {
    drawPixi() {
      document.getElementById('main').appendChild(this.app.view)
      for (let i = 0; i < this.starAmount; i++) {
          const star = {
              sprite: new PIXI.Sprite(this.starTexture),
              z: 0,
              x: 0,
              y: 0,
          };
          star.sprite.anchor.x = 0.5;
          star.sprite.anchor.y = 0.7;
          randomizeStar(star, true);
          this.app.stage.addChild(star.sprite);
          this.stars.push(star);
      }
      function randomizeStar(star, initial) {
          star.z = initial ? Math.random() * 2000 : 0 + Math.random() * 1000 + 2000;

          // Calculate star positions with radial random coordinate so no star hits the camera.
          const deg = Math.random() * Math.PI * 2;
          const distance = Math.random() * 50 + 1;
          star.x = Math.cos(deg) * distance;
          star.y = Math.sin(deg) * distance;
      }

      this.app.ticker.add((delta) => {
          // Simple easing. This should be changed to proper easing function when used for real.
          this.speed += (this.warpSpeed - this.speed) / 20;
          this.cameraZ += delta * 10 * (this.speed + this.baseSpeed);
          for (let i = 0; i < this.starAmount; i++) {
              const star = this.stars[i];
              if (star.z < this.cameraZ) randomizeStar(star);

              // Map star 3d position to 2d with really simple projection
              const z = star.z - this.cameraZ;
              star.sprite.x = star.x * (this.fov / z) * this.app.renderer.screen.width + this.app.renderer.screen.width / 2;
              star.sprite.y = star.y * (this.fov / z) * this.app.renderer.screen.width + this.app.renderer.screen.height / 2;

              // Calculate star scale & rotation.
              const dxCenter = star.sprite.x - this.app.renderer.screen.width / 2;
              const dyCenter = star.sprite.y - this.app.renderer.screen.height / 2;
              const distanceCenter = Math.sqrt(dxCenter * dxCenter + dyCenter * dyCenter);
              const distanceScale = Math.max(0, (2000 - z) / 2000);
              star.sprite.scale.x = distanceScale * this.starBaseSize;
              // Star is looking towards center so that y axis is towards center.
              // Scale the star depending on how fast we are moving, what the stretchfactor is and depending on how far away it is from the center.
              star.sprite.scale.y = distanceScale * this.starBaseSize + distanceScale * this.speed * this.starStretch * distanceCenter / this.app.renderer.screen.width;
              star.sprite.rotation = Math.atan2(dyCenter, dxCenter) + Math.PI / 2;
          }
      });

    },
    onClickChange() {
      if (this.$store.state.mainCheck) {
        this.warpSpeed = this.warpSpeed > 0 ? 0 : 1;
        
        if (this.TimerOn) {
          clearTimeout(this.timer);
          this.TimerOn = false;
          this.warpSpeed = 0
        } else {
          this.TimerOn = true;
          this.warpSpeed = 1
          this.timer = setTimeout(() => {
            this.$store.commit("MainChange");
            this.TimerOn = false; // Reset the TimerOn flag
          }, 5000);
        }
      }
    }
  },
  mounted() {
    this.drawPixi()
  }
}

</script>
