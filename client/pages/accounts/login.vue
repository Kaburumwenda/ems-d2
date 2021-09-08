<template>
	<div>
	 <div id="particles-js">
        <div class="inside-particles">
            <div>
				<div class="card-background">
				<ScCard>
				<ScCardBody>
					<div class="sc-login-page-logo">
						<img v-rjs="require('~/assets/img/logo_alt@2x.png')" :src="appLogo" alt="">
					</div>
					<div class="sc-login-page-logo sc-login-page-logo-light">
						<img v-rjs="require('~/assets/img/logo_alt.png')" :src="appLogoLight" alt="">
					</div>
					<div id="sc-login-form" class="sc-toggle-login-register sc-toggle-login-password">
						<div class="sc-login-page-inner">
							<div class="uk-margin-medium">
								<ScInput v-model="loginData.login">
									<label>
										Email/Login
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="loginData.password" type="password">
									<label>
										Password
									</label>
								</ScInput>
								<div class="uk-margin-small-top uk-text-small uk-text-right@s">
									<a href="javascript:void(0)" class="sc-link" data-uk-toggle="target: .sc-toggle-login-password; animation: uk-animation-scale-up">
										Forgot Password?
									</a>
								</div>
							</div>
							<div class="uk-margin-large-top">
								<nuxt-link to="/" class="sc-button sc-button-large sc-button-block sc-button-danger">
									Sign In
								</nuxt-link>
								<div class="uk-margin-large-top uk-text-center">
									<span class="sc-color-secondary">
										Don't have an account?
									</span>
									<div>
										<a href="javascript:void(0)" class="sc-text-semibold" data-uk-toggle="target: .sc-toggle-login-register; animation: uk-animation-scale-up">
											Sign Up
										</a>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div id="sc-register-form" class="sc-toggle-login-register" hidden>
						<div class="sc-login-page-inner">
							<div class="uk-margin-medium">
								<ScInput v-model="registerData.name">
									<label>
										Name
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="registerData.email">
									<label>
										Email
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="registerData.password">
									<label>
										Password
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-large-top">
								<button class="sc-button sc-button-large sc-button-block sc-button-secondary">
									Sign Up
								</button>
								<div class="uk-margin-large-top uk-flex uk-flex-middle uk-flex-center">
									<a href="javascript:void(0)" class="sc-text-semibold" data-uk-toggle="target: .sc-toggle-login-register; animation: uk-animation-scale-up">
										Back to login form
									</a>
								</div>
							</div>
						</div>
					</div>
					<div id="sc-password-form" class="sc-toggle-login-password" hidden>
						<div class="sc-login-page-inner">
							<div class="uk-margin-medium">
								Please enter your email address. You will receive a link to reset your password.
							</div>
							<div class="uk-margin-medium">
								<ScInput v-model="recoverPassEmail">
									<label>
										Email
									</label>
								</ScInput>
							</div>
							<div class="uk-margin-large-top">
								<button class="sc-button sc-button-large sc-button-block sc-button-primary">
									Reset Password
								</button>
								<div class="uk-margin-large-top uk-flex uk-flex-middle uk-flex-center">
									<a href="javascript:void(0)" class="sc-text-semibold" data-uk-toggle="target: .sc-toggle-login-password; animation: uk-animation-scale-up">
										Back to login form
									</a>
								</div>
							</div>
						</div>
					</div>
				</ScCardBody>
			</ScCard>
				</div>
			</div>
	    </div>
	</div>
	</div>

</template>

<script>
import ScInput from '~/components/Input'

export default {
	name: 'LoginPage',
    layout: 'login_page',
	components: {
		ScInput
	},
	data: () => ({
		loginData: {
			login: '',
			password: ''
		},
		registerData: {
			name: '',
			email: '',
			password: ''
		},
		recoverPassEmail: ''
	}),

	mounted(){
       this.getParticles();
   },
   methods:{
       getParticles(){
           particlesJS.load('particles-js', '../../particles.json', function() {
              console.log('callback - particles.js config loaded');
           });
       }
   },

	head () {
		return {
			'title': 'EMS Admin Login Page'
		}
	},
	computed: {
		appLogo () {
			return require('~/assets/img/logo_alt.png');
		},
		appLogoLight () {
			return require('~/assets/img/logo.png');
		}
	}
}
</script>
<style scoped>
.card-background{
	background: white;
	padding: 20px 20px 20px 20px;
	margin: auto;
	top: 50%;
	left: 50%;
	width: 400px;
	opacity: 0.8;
	position:absolute;
	transform: translate(-50%, -50%);
}
#particles-js{
	height: 100vh;
}
@media only screen and (max-width: 768px) {
	.card-background{
		width: 90vw !important;
	}
}
</style>

