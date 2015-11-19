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
            var client = new HttpClient();
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
                    response = await client.GetAsync(uri);
                    if (response.IsSuccessStatusCode)
                    {
                        var bmp = new Bitmap(await response.Content.ReadAsStreamAsync());
                        var fm = new Form1();
                        fm.pictureBox1.Image = bmp;
                        fm.ShowDialog();
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