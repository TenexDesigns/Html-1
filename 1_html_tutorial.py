/*
 *              ************* HTML Text Formating ***********
 *       The following tags are used for Text formatting
 *       <b>             - Bold text
 *       <strong>        - Important text
 *       <i>             - Italic text
 *       <em>            - Emphasized text
 *       <mark>          - Marked text
 *       <small>         - Small text
 *       <del>           - Deleted text
 *       <ins>           - Inserted text
 *       <sub>           - Subscript text
 *       <sup>           - Superscript text
 *
 *                 
 *                      ************* HTML empty tags ***********
 *          These tags do not require a clossing tag
 *                 <img>                   - This is where the image is put 
 *                 <br>                    - Goes to the next line
 *                 <hr>                    - puts a horizontal line
 *
 *
 *
 *                    ************* HTML Attributes ***********
 *
 *               These provide additional information about the html tags 
 *               They are always put on the oprning tag
 *               They always come in key:value pairs   e.g type="text"
 *                
 *
 *
 *                 ************* Anchor Tags ***********
 *               These are used to lead to other links. The links is put in the href i.e href="link" and the text to be seen on the html is put between the anchor tags 
 *             <a href="https://google.com" >Google</a>
 *
 *              To make the link open on another tab ,instead of the current tab,We use the  target="_blank"
 *                     <a href="https://google.com" target="_blank">Google</a>
 *
 *             To put the link in an image,We put the image tag betwwen the anchor tags   
 *                     <a href="https://google.com" target="_blank">
 *                                                     <img src="https://pexels.com/mountains">            
 *                                                                 </a>
 *
 *             We can use the ancor tag and id to navigate to a section of the webpage
 *                   <P id="top">This is at the to of the webpage</p>
 *
 *                 Now at the bottom ,we can use an ancor tag with href of the id of the section we want to navigate to. We put a hash before the id
 *                   <P id="top">This is at the to of the webpage</p>
 *                        <a href="#top">Go top</a>
 *
 *
 *                                ************* Tables ***********
 *             We create tables using the tables tag                                   <table><table/>
 *             Inside the table ,there is the table head and table body
 *                           <thead><thead/>
 *                           <tbody><body/>
 *             Inside the  table head we need to give the table row 
 *                            <tr><tr/>
 *             Inside the table row we to give the row titiles in the th
 *                   <thead>
 *                       <tr>
 *                            <th>Name<th/>
 *                            <th>Age<th/>
 *                       <tr>
 *                    <thead>
 *             Inside the table body  we need to give table row and table data 
 *                      <tbody>
 *                            <tr>
 *                              <td>George<td/>
 *                              <td>34<td/>
 *                            <tr>
 *                      <tbody>
 *
 *
 *
 *
 *
 *                                ************* iFrame ***********
 *                      This is used to display websites in a  mini window
 *                      we put the link of the website in the src attribute tag
 *                                 <iframe src="hhtps://wwww.facebook.com"><iframe/>
 *
 *                      We can customize the size of the mini window with height and width 
 *                                 <iframe src="hhtps://wwww.facebook.com" width="500" height="500"><iframe/>
 *
 *
 *                     To emmbed a youtube video ,Go to the share button on the video and click on the emmbed option.
 *                      This will give you an iframe with the emmbeded video to put on your website
 *                          <iframe width="560" height="315" src="https://www.youtube.com/embed/hggN04aCBDQ"
 *                            title="YouTube video player" frameborder="0"
 *                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
 *                             picture-in-picture" allowfullscreen></iframe>
 *
 *
 *                                ************* Form input types and Label ***********
 *
 *                                  We use label to give user info on the input to be given
 *                                  To associate the label with the input we use (id) in the input and (for) in the label
 *                                    
 *                                  <label for="user">Username<label/>
 *                                    <input type="text" id="user">
 *
 *
 *
 *                                ************* Form Input Types  ***********
 *                    We use the value attribute to put a  default value tat will initialy be in the input tag on load
 *                    We can Increase the size of the input box by using the size attribute
 *                    To make the input readonly and non editable we use readonly="true"
 *                    To disable the input tag we use disable="true"
 *                              <input type="checkbox">
 *                              <input type="color" >
 *                              <input type="date">
 *                              <input type="email" value="name">
 *                              <input type="radio">
 *                              <input type="url" value="name">
 *                              <input type="text" value="name">
 *                              <input type="number">
 *                              <input type="password">
 *                              <input type="range" value="name">
 *                              <input type="search" value="name">
 *                              <input type="submit">
 *                              <input type="textarea">                     //We can increase the sie of the text area using cols and rows
 *
 *
 *
 *                                ************* Form Validation  ***********
 *                                    A form has default validations to validate input values in it e.g for email,number ,age e.t.c
 *                                    To prevent this default validations and put our own validations we use the 
 *                                    novalidate attribute on the form tag
 *                                   <form novalidate> <form/>
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *                                ************* Radio Button and name ***********
 *              Radio buttons need to have same name so that only one of them can be selected
 *
 *                        <input type="radio" value="George" name="do" >
 *                        <input type="radio" value="Eliud" name="do">
 *                        <input type="radio" value="Boni" name="do">
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *

























*/
