from flask import Flask, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        # Retrieve the entered number from the form
        entered_number = request.form['number']
        # Redirect to the result page with the entered number as a parameter
        return redirect(url_for('result', number=entered_number))
    return """
           <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>NPS PU COLLEGE</title>
              <style>
                body {
                  font-family: 'Arial', sans-serif;
                  background-color: #f8f9fa;
                  margin: 0;
                  padding: 0;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  height: 100vh;
                }

                .form-container {
                  background-color: #ffffff;
                  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                  padding: 30px;
                  border-radius: 10px;
                  text-align: center;
                  max-width: 500px;
                  width: 100%;
                }

                h1 {
                  color: #343a40;
                  display: flex;
                  align-items: center;
                  font-family: "Times New Roman", Times, serif;
                }

                h3 {
                  color: #195057;
                  margin-bottom: 15px;
                }

                h5 {
                  color: #495057;
                  margin-bottom: 15px;
                }

                label {
                  display: block;
                  margin-bottom: 10px;
                  color: #133057;
                }

                input {
                  width: 100%;
                  padding: 12px;
                  box-sizing: border-box;
                  margin-bottom: 20px;
                  border: 1px solid #ced4da;
                  border-radius: 6px;
                  background-color: #f8f9fa;
                  color: #495057;
                }

                button {
                  background-color: #28a745;
                  color: #ffffff;
                  padding: 12px 20px;
                  border: none;
                  border-radius: 6px;
                  cursor: pointer;
                }

                button:hover {
                  background-color: #218838;
                }

                .container {
                  text-align: center;
                  display: flex;
                  align-items: center;
                  justify-content: center;
                }

                .container img {
                  padding-right: 40px;
                  padding-left: 40px;
                  max-width: 100px;
                }

                /* Media queries for responsiveness */
                @media (max-width: 768px) {
                  .form-container {
                    padding: 20px;
                  }

                  h1 {
                    flex-direction: column;
                  }

                  .container img {
                    padding-right: 0;
                    padding-left: 0;
                    margin-bottom: 10px;
                  }
                }

                @media (max-width: 480px) {
                  .form-container {
                    padding: 15px;
                  }

                  h1 {
                    font-size: 24px;
                  }

                  h3 {
                    font-size: 18px;
                  }

                  h5 {
                    font-size: 16px;
                  }

                  label {
                    font-size: 14px;
                  }

                  input {
                    padding: 8px;
                  }

                  button {
                    padding: 8px 16px;
                    font-size: 14px;
                  }
                }
              </style>
            </head>
            <body>
              <div class="form-container">
                <div class="container">
                  <h1>
                    <img src="/static/Picture2.jpg" alt="Logo Image">
                    National Public PU College, Kalaburgi
                    <img src="/static/Picture1.jpg" alt="Logo Image">
                  </h1>
                </div>
                <br>
                <h3>PUC-I ANNUAL EXAMINATION 2023-2024</h3>
                <form method="post" action="/">
                  <label for="number">(Enter Roll Number. NPSHCXXXXX )</label>
                  <input type="text" id="number" name="number" maxlength="10" oninput="validateInput(this)" required>
                  <button type="submit" style="font-weight: bold;">Submit</button>
                </form>
              </div>
            </body>
            </html>

    """



@app.route('/result/<number>')
def result(number):
    number=number.upper()
    data={}
    with open('/home/NPSPUCOLLEGE/puresults/Final_Exam_Results.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data[row[2]]=row
    #print(data['2'])
    if  number not in data.keys():
        return """
                  <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Booklet No. Error</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f8f8f8;
                        text-align: center;
                        padding: 50px;
                    }

                    h1 {
                        color: #ff4444;
                        font-size: 36px;
                        margin-bottom: 20px;
                    }

                    h3 {
                        color: #000000;
                        margin-bottom: 20px;
                    }

                    button {
                        padding: 10px 20px;
                        font-size: 18px;
                        font-weight: bold;
                        background-color: green;
                        color: #fff;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                    }

                    /* Media queries for responsiveness */
                    @media (max-width: 768px) {
                        h1 {
                            font-size: 28px;
                        }

                        h3 {
                            font-size: 16px;
                        }

                        button {
                            font-size: 16px;
                        }
                    }

                    @media (max-width: 480px) {
                        h1 {
                            font-size: 24px;
                        }

                        h3 {
                            font-size: 14px;
                        }

                        button {
                            font-size: 14px;
                            padding: 8px 16px;
                        }
                    }
                </style>
            </head>
            <body>
                <h1>Roll Number NOT Found !!</h1>
                <h3>Enter correct Roll Number (NPSHCXXXXX) and Try Again.</h3>
                <form method="get" action="/">
                    <button type="submit">Go Back</button>
                </form>
            </body>
            </html>

        """
    d=data[number]
    page="""<!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>PUC-1 Annual Examination Results</title>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');

                    body {
                        font-family: 'Lato', sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: light-grey;
                    }

                    .container {
                        max-width: 800px;
                        margin: 20px auto;
                        padding: 20px;
                        background-color: #fff;
                        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                        border: 1px solid #ddd;
                        border-radius: 10px;
                    }

                    h2 {
                        text-align: center;
                        color: #195057;
                    }

                    h1 {
                        color: #343a40;
                        display: flex;
                        align-items: center;
                        font-family: "Times New Roman", Times, serif;
                    }


                    table {
                        border-collapse: collapse;
                        width: 100%;
                        margin-top: 20px;
                        border: 1px solid #ddd;
                    }

                    th,
                    td {
                        padding: 12px;
                        text-align: left;
                        border: 1px solid #ddd;
                    }

                    th {
                        background-color: #f5f5f5;
                        font-weight: bold;
                    }

                    .container1 {
                        text-align: center;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }

                        .button {
                          background-color: green;
                          border: none;
                          color: white;
                          padding: 15px 32px;
                          text-align: center;
                          text-decoration: none;
                          display: inline-block;
                          font-size: 16px;
                          margin: 4px 2px;
                          cursor: pointer;
                          border-radius: 10px;
                          text-decoration: underline;
                        }
                        .button:hover {
                          background-color: #45a049;
                        }


                </style>

              <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
            	<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
            	<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>

            </head>
        """
    page+=f"""
            <body>
                <div id="divID" class="">

                    <div class="container1">
                        <h1>
                            <img src="/static/Picture2.jpg" alt="Logo Image">
                            NATIONAL PUBLIC PU COLLEGE KALABURAGI
                            <img src="/static/Picture1.jpg" alt="Logo Image">
                        </h1>
                    </div>
                    <h2>PUC-1 ANNUAL EXAMINATION 2023-2024</h2>
                    <h2 style="font-weight: bold;color:#00008B; text-decoration: underline;">RESULTS </h2>
                    <hr>
                    <table>
                        <tr>
                            <th>Name</th>
                            <td>{d[3]}</td>
                            <th>Father's Name</th>
                            <td>{d[4]}</td>
                        </tr>
                        <tr>
                            <th>Mother's Name</th>
                            <td>{d[5]}</td>
                            <th>Roll Number</th>
                            <td>{d[2]}</td>
                        </tr>
                        <tr>
                            <th>SATS Number</th>

                            <td colspan="3">{d[1]}</td>
                        </tr>
                        <tr>

                            <th colspan="4" style="text-align:center"><b>PART-A</b></th>


                        </tr>
                        <tr >
                            <th style="text-align:left">SUBJECT</th>
                            <th style="text-align:center">THEORY</th>
                            <th style="text-align:center">INTERNAL</th>
                            <th style="text-align:center">TOTAL</th>
                        </tr>
                        <tr>
                            <td style="text-align:left">ENGLISH</td>
                            <td style="text-align:center">{d[6]}</td>
                            <td style="text-align:center">{d[7]}</td>
                            <td style="text-align:center">{d[8]}</td>
                        </tr>
                        <tr>
                            <td>KANNADA / HINDI</td>
                            <td style="text-align:center">{d[9]}</td>
                            <td style="text-align:center">{d[10]}</td>
                            <td style="text-align:center">{d[11]}</td>
                        </tr>
                        <tr>
                            <th>PART-A TOTAL</th>
                            <td></td>
                            <td></td>
                            <td  style="text-align:center;font-weight: bold;">{d[12]}</td>

                        </tr>
                        <tr>
                            <th colspan="4" style="text-align:center"><b>PART-B</b></th>
                        </tr>
                        <tr>
                            <th>SUBJECT</th>
                            <th style="text-align:center">THEORY</th>
                            <th style="text-align:center">PRACTICAL / INTERNAL</th>
                            <th style="text-align:center">TOTAL</th>
                        </tr>
                        <tr>
                            <td>PHYSICS</td>
                            <td style="text-align:center">{d[13]}</td>
                            <td style="text-align:center">{d[14]}</td>
                            <td style="text-align:center">{d[15]}</td>
                        </tr>
                        <tr>
                            <td>CHEMISTRY</td>
                            <td style="text-align:center">{d[16]}</td>
                            <td style="text-align:center">{d[17]}</td>
                            <td style="text-align:center">{d[18]}</td>
                        </tr>
                        <tr>
                            <td>MATHEMATICS</td>
                            <td style="text-align:center">{d[19]}</td>
                            <td style="text-align:center">{d[20]}</td>
                            <td style="text-align:center">{d[21]}</td>
                        </tr>
                        <tr>
                            <td>BIOLOGY / COMPUTER SCIENCE</td>
                            <td style="text-align:center">{d[22]}</td>
                            <td style="text-align:center">{d[23]}</td>
                            <td style="text-align:center">{d[24]}</td>
                        </tr>
                        <tr>
                            <th>PART-B TOTAL</th>
                            <td></td>
                            <td></td>
                            <td style="text-align:center;font-weight: bold;">{d[25]}</td>

                        </tr>
                        <tr>
                            <th>GRAND TOTAL</th>
                            <td colspan="3" style="text-align:left;font-weight: bold;">{d[26]}</td>

                        </tr>
                        <tr>
                            <th>PERCENTAGE</th>
                            <td colspan="3" style="text-align:left;font-weight: bold;">{d[27]}%</td>
                        </tr>
                        <tr>
                            <th>RANK</th>
                            <td colspan="3" style="text-align:left;font-weight: bold;">{d[28]}</td>
                        </tr>
                        <tr>
                            <th>REMARKS</th>
                            <td colspan="3" style="text-align:center;font-weight: bold;" bgcolor="lightgreen">{d[29]}</td>
                        </tr>
                        <tr>
                            <td colspan="4" style="text-align:center">In academic alliance with<br>HANCHINMANI INSTITUTES DHARWAD
                            </td>
                        </tr>
                        <tr>
                            <td colspan="4" style="text-align:center; text-decoration: underline;">  <input type="button" value="To Download The Result Click Here !!" onclick="convertHTMLtoPDF()" class="button"> </td>
                        """
    page+="""              <script type="text/javascript">
                        		function convertHTMLtoPDF() {
                        			const { jsPDF } = window.jspdf;

                        			let doc = new jsPDF('l', 'mm', [1500, 1400]);
                        			let pdfjs = document.querySelector('#divID');

                        			doc.html(pdfjs, {
                        				callback: function(doc) {
                        					doc.save("result_pu.pdf");
                        				},
                        				x: 12,
                        				y: 12
                        			});
                        		}
                        	</script>

                        </tr>
                    </table>
                </div>
            </body>

            </html>
    """
    return f'{page}'
