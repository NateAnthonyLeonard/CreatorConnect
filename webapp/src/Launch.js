import React, { useState } from 'react'
import ReactDOM from 'react-dom';
import './CreatorConnect.css';
import { Route, BrowserRouter as Router, Link, Redirect } from 'react-router-dom';
import {render} from 'react-dom';
import { bool } from 'prop-types';

//*This is the Login Component that will prompt users to either sign up or login to CreatorConnect*/

//NOTE- YOUR HTML CODE NEEDS TO BE AT WRAPPED AROUND A DIV OBJECT.
const STYLE = {
  SPAN:
  {
    fontSize: "1.5em"
  },
  BETA:
  {
    fontSize: ".25em"
  }
}

/*declaration of the Launch class that will hold form data*/
class Launch extends React.Component {}

/*This function will be used to handle the form*/
export default function MultipleSelect() {
  const existingUser = "Existing User? Click here"
  const newUser = "New User? Click Here"
  //react hooks are used in a rather unconventional manner here. Allows for uniform asynchrenous functionality later on
  const boolArray = [true, false]  
  const [registration, hideRegistration] = useState(boolArray[0]);
  const [login, setLogin] = useState(boolArray[1]);
  const [button, setButton] = useState(existingUser);
  const [skill, setSkill] = React.useState([]);
  let newUserData = {
    firstName: '',
    lastName: '',
    email: ' ',
    password: ' ',
    gradDate: ' ',
    skills: [],
    dateCreated: Date()     //add a timestamp going forward
  }
 
  /*Trigger buttons that use hooks to either show or hide the login/signup option*/
  function triggerRegistration() {hideRegistration(!registration)}
  function triggerLogin() {setLogin(!login)}
  function triggerButton() {
    if(button == existingUser)
    {
      setButton(newUser)
    }
    else
    {
      setButton(existingUser)
    }
  }

  return (
    <div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap-select@1.13.9/dist/js/bootstrap-select.min.js"></script>
      <div className ="bothDivs">
        <div className = "leftDiv">
          <img img src="/images/logo.png" alt="hub logo" className = "hubLogo"></img>
        </div>
        <div className = "rightDiv">
          <div className = "signUpOrIn">
            <div className = "CreatorConnectLogo">
            <h4 className="launchText"><span style={STYLE.SPAN}>C</span>reator<span style={STYLE.SPAN}>C</span>onnect<span style={STYLE.BETA}>BETA</span></h4>

              <div className="informationWrap">
              <div className = "information">

              {/*first form, the new user form*/}
              {registration && <form action = 'http://orlandokenny.pythonanywhere.com/register' method = 'POST'>
                  <input required className="inputBox" type="text" name="firstName" placeholder="First Name" ref={input => newUserData.firstName = input}></input>
                
                  <input required className="inputBox" type="text" name="lastName" placeholder="Last Name" ref={input => newUserData.lastName = input}></input>
                
                  <input required className="inputBox" type="email" name="fsuEmail" placeholder="FSU E-mail (lowercase)" pattern=".+@.+.fsu.edu"  ref={input => newUserData.email = input}></input>
             
                  <input required className="inputBox" type="password" name="password" placeholder="Password" ref={input => newUserData.password = input}></input>
                
                  {/*VERIFY PASSWORD INPUT BOX... WILL BE LEFT OUT FOR BETA AND FOCUS GROUP RELEASE*/}
                
                <div className="dropdown">
                  <select required name="gradYear" class="ui fluid dropdown">
                      <option value="">Graduation Year</option>
                      <option value="2020">2020</option>
                      <option value="2021">2021</option>
                      <option value="2022">2022</option>
                      <option value="2023">2023</option>
                      <option value="2024">2024</option>
                      <option value="2025">2025</option>
                      <option value="2026">2026</option>
                  </select>
                </div>

                  {/*FORCE LOWERCASE INPUT GOING FORWARD*/}
                  <div className="dropdown">
                    <select required name="firstSkill" class="ui fluid dropdown">
                      <option value="">Skill #1 (REQUIRED)</option>
                      <option value="App Development">App Development</option>
                      <option value="Electrical Circuits">Electrical Circuits</option>
                      <option value="Laser Cutting">Laser Cutting</option>
                      <option value="Computer Programming">Computer Programming</option>
                      <option value="3D Design">3D Design</option>
                      <option value="Brand Development">Brand Development</option>
                      <option value="Design Thinking">Design Thinking</option>
                      <option value="Digital Fabrication/3D Printing">Digital Fabrication/3D Printing</option>
                      <option value="Social Entrepreneurship">Social Entrepreneurship</option>
                      <option value="Entrepreneurship">Entrepreneurship</option>
                      <option value="Game/VR Design">Game/VR Design</option>
                      <option value="Graphic Design">Graphic Design</option>
                      <option value="Digital Photography">Digital Photography</option>
                      <option value="User Experience (UX) Design">User Experience (UX) Design</option>
                      <option value="Social Media Marketing">Social Media Marketing</option>
                      <option value="Video Production">Video Production</option>
                      <option value="Web Design">Web Design</option>
                      <option value="Web Development">Web Development</option>
                    </select>
                </div>

                <div className="dropdown">
                    <select name="secondSkill" class="ui fluid dropdown">
                      <option value="">Skill #2</option>
                      <option value="App Development">App Development</option>
                      <option value="Electrical Circuits">Electrical Circuits</option>
                      <option value="Laser Cutting">Laser Cutting</option>
                      <option value="Computer Programming">Computer Programming</option>
                      <option value="3D Design">3D Design</option>
                      <option value="Brand Development">Brand Development</option>
                      <option value="Design Thinking">Design Thinking</option>
                      <option value="Digital Fabrication/3D Printing">Digital Fabrication/3D Printing</option>
                      <option value="Social Entrepreneurship">Social Entrepreneurship</option>
                      <option value="Entrepreneurship">Entrepreneurship</option>
                      <option value="Game/VR Design">Game/VR Design</option>
                      <option value="Graphic Design">Graphic Design</option>
                      <option value="Digital Photography">Digital Photography</option>
                      <option value="User Experience (UX) Design">User Experience (UX) Design</option>
                      <option value="Social Media Marketing">Social Media Marketing</option>
                      <option value="Video Production">Video Production</option>
                      <option value="Web Design">Web Design</option>
                      <option value="Web Development">Web Development</option>
                    </select>
                </div>

                <div className="dropdown">
                    <select name="thirdSkill" class="ui fluid dropdown">
                      <option value="">Skill #3</option>
                      <option value="App Development">App Development</option>
                      <option value="Electrical Circuits">Electrical Circuits</option>
                      <option value="Laser Cutting">Laser Cutting</option>
                      <option value="Computer Programming">Computer Programming</option>
                      <option value="3D Design">3D Design</option>
                      <option value="Brand Development">Brand Development</option>
                      <option value="Design Thinking">Design Thinking</option>
                      <option value="Digital Fabrication/3D Printing">Digital Fabrication/3D Printing</option>
                      <option value="Social Entrepreneurship">Social Entrepreneurship</option>
                      <option value="Entrepreneurship">Entrepreneurship</option>
                      <option value="Game/VR Design">Game/VR Design</option>
                      <option value="Graphic Design">Graphic Design</option>
                      <option value="Digital Photography">Digital Photography</option>
                      <option value="User Experience (UX) Design">User Experience (UX) Design</option>
                      <option value="Social Media Marketing">Social Media Marketing</option>
                      <option value="Video Production">Video Production</option>
                      <option value="Web Design">Web Design</option>
                      <option value="Web Development">Web Development</option>
                    </select>
                </div>

                <div className="dropdown">
                    <select name="fourthSkill" class="ui fluid dropdown">
                      <option value="">Skill #4</option>
                      <option value="App Development">App Development</option>
                      <option value="Electrical Circuits">Electrical Circuits</option>
                      <option value="Laser Cutting">Laser Cutting</option>
                      <option value="Computer Programming">Computer Programming</option>
                      <option value="3D Design">3D Design</option>
                      <option value="Brand Development">Brand Development</option>
                      <option value="Design Thinking">Design Thinking</option>
                      <option value="Digital Fabrication/3D Printing">Digital Fabrication/3D Printing</option>
                      <option value="Social Entrepreneurship">Social Entrepreneurship</option>
                      <option value="Entrepreneurship">Entrepreneurship</option>
                      <option value="Game/VR Design">Game/VR Design</option>
                      <option value="Graphic Design">Graphic Design</option>
                      <option value="Digital Photography">Digital Photography</option>
                      <option value="User Experience (UX) Design">User Experience (UX) Design</option>
                      <option value="Social Media Marketing">Social Media Marketing</option>
                      <option value="Video Production">Video Production</option>
                      <option value="Web Design">Web Design</option>
                      <option value="Web Development">Web Development</option>
                    </select>
                </div>

                <div className="dropdown">
                    <select name="fifthSkill" class="ui fluid dropdown">
                      <option value="">Skill #5</option>
                      <option value="App Development">App Development</option>
                      <option value="Electrical Circuits">Electrical Circuits</option>
                      <option value="Laser Cutting">Laser Cutting</option>
                      <option value="Computer Programming">Computer Programming</option>
                      <option value="3D Design">3D Design</option>
                      <option value="Brand Development">Brand Development</option>
                      <option value="Design Thinking">Design Thinking</option>
                      <option value="Digital Fabrication/3D Printing">Digital Fabrication/3D Printing</option>
                      <option value="Social Entrepreneurship">Social Entrepreneurship</option>
                      <option value="Entrepreneurship">Entrepreneurship</option>
                      <option value="Game/VR Design">Game/VR Design</option>
                      <option value="Graphic Design">Graphic Design</option>
                      <option value="Digital Photography">Digital Photography</option>
                      <option value="User Experience (UX) Design">User Experience (UX) Design</option>
                      <option value="Social Media Marketing">Social Media Marketing</option>
                      <option value="Video Production">Video Production</option>
                      <option value="Web Design">Web Design</option>
                      <option value="Web Development">Web Development</option>
                    </select>
                </div>
                <button className="inputBox" type="submit">Submit!</button>
                </form>}

                {/*second form, the existing user form*/}
                {login && <form action = 'http://orlandokenny.pythonanywhere.com/login' method = 'POST'>
                    <input required className="inputBox" type="text" name="fsuEmail" placeholder="FSU E-mail"></input>
                  <input required className="inputBox" type="password" name="password" placeholder="Password"></input>
                  <button className="inputBox" type="submit">Log In</button>
                </form>} 
                
                {/*button that triggers between the new user and the existing user forms*/}
                <button className="inputBox" onClick={() => {
                  triggerRegistration();
                  triggerLogin();
                  triggerButton();
                }}>
                  {button}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  )
}
