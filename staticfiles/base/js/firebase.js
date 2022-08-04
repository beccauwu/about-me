// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAos1C-5as5wRU0p18J6dba-mVIm23ic5I",
  authDomain: "about-me-rebecca.firebaseapp.com",
  projectId: "about-me-rebecca",
  storageBucket: "about-me-rebecca.appspot.com",
  messagingSenderId: "470470984330",
  appId: "1:470470984330:web:d0efe95e1b4fcdee4c2373",
  measurementId: "G-5B5Q256F14",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

