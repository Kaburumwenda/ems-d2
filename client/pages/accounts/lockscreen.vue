<template>
 <div id="particles-js">
    <div>
    <div id="lockscreen-main-con">
        <div id="lockscreen-con">
            <div>
                <h1 class="text-center">EMS</h1>
               
                <p class="text-center"><b>John Doe</b></p>
            </div>
            <form>
                <div class="text-center">
                    <!-- <ScInput>
                        <label>Enter password to continue</label>
                    </ScInput> -->
                    <input class="lock-input" placeholder="Enter password to continue ...">
                </div>
                <div class="help-block text-center">
                    Enter your password to retrieve your session
                </div>
                <br>
                <div class="text-center">
                    <nuxt-link to="/accounts/login">Or sign in as a different user</nuxt-link>
                </div>
            </form>
        </div>
    </div>

    </div>
    
 </div>
</template>


<script>
import ScInput from '~/components/Input'
export default {
   layout:"login_page",
   components: {
		ScInput
	},
   mounted(){
       this.getParticles();
   },
   methods:{
       getParticles(){
           particlesJS.load('particles-js', '../../particles.json', function() {
              console.log('callback - particles.js config loaded');
           });
       }
   }
}
</script>

<style scoped>
body{
    background-image: linear-gradient(to top, #0ba360 0%, #3cba92 100%);
    width: 100vw;
}
#lockscreen-main-con{
    
}
#lockscreen-con{
    background: white;
	padding: 20px 20px 20px 20px;
	top: 50%;
	left: 50%;
	opacity: 0.8;
	width: 400px;
	position:absolute;
    transform: translate(-50%, -50%);
}
#particles-js{
    height: 100vh;
    position: relative;
}
.lock-input{
    width:80%;
    margin-bottom: 10px;
    background: transparent;
    border-top: none;
    border-left: none;
    border-right: none;
    outline: none;
}
@media only screen and (max-width: 768px) {
	#lockscreen-con{
		width: 80vw !important;
	}
}
</style>