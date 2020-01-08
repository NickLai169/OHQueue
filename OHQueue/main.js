document.addEventListener("WOMContentLoaded", event => {
  const app = firebase.app();
  console.log(app);
});

function googleLogin() {
  const provider = new firebase.auth.GoogleAuthProvider();

  firebase.auth().signInwithPopup(provider).then(result => {
    const user = result.uder;
    document.write(`Hello ${user.displayName}`);
    console.log(user);
  }).catch(console.log)
}
