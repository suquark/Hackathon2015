using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;
using System.Text;
using System.Net.Http.Headers;
using System.Web;
using System.Drawing;
namespace Hackathon2015
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            //Application.EnableVisualStyles();
            //Application.SetCompatibleTextRenderingDefault(false);
            //Application.Run(new Form1());
            MakeRequest();
            Console.WriteLine("Hit ENTER to exit...");
            Console.ReadLine();
        }




        static async void MakeRequest()
        {

            var queryString = HttpUtility.ParseQueryString(string.Empty);

            // Request headers
            //client.DefaultRequestHeaders.Add("Content-Type", "application/octet-stream");
            //client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", "{subscription key}");

            // Request parameters
            //queryString["analyzesFaceLandmarks"] = "false";
            //queryString["analyzesAge"] = "false";
            //queryString["analyzesGender"] = "false";
            //queryString["analyzesHeadPose"] = "false";
            var uri = "http://192.168.43.161:8888/poll" + queryString;
            var uriimage = "http://192.168.43.161:8888/image" + queryString;
            HttpResponseMessage response;
            // Request body
            //byte[] byteData = Encoding.UTF8.GetBytes("{body}");

            //using (var content = new ByteArrayContent(byteData))
            //{
            //    content.Headers.ContentType = new MediaTypeHeaderValue("< your content type, i.e. application/json >");
            //    response = await client.PostAsync(uri, content);
            //}
            while (true)
            {
                try
                {
                    using (var client = new HttpClient())
                    {
                        response = await client.GetAsync(uri);
                        if (response.IsSuccessStatusCode)
                        {
                            var fm = new Form1();
                            fm.textBox1.Text = await response.Content.ReadAsStringAsync();
                            using (var clienti = new HttpClient())
                            {
                                //fm.pictureBox1.Image = new Bitmap(await clienti.GetStreamAsync(uriimage));
                                var ntwk = new Microsoft.VisualBasic.Devices.Network();

                                ntwk.DownloadFile(uriimage, "temp.jpg", "", "", false, 100, true);
                                fm.pictureBox1.Image = new Bitmap("temp.jpg");
                            }
                            fm.ShowDialog();
                        }
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
                await Task.Delay(2000);
            }
        }
    }
}