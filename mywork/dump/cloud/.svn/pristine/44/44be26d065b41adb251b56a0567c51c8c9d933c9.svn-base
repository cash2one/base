// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.ExeHost
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="Program.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>Program<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.Text;
using Cytel.Cloud.DataInteractiveService.Contract;
using Cytel.Cloud.DataInteractiveService.Service;

/// <summary>
/// The ExeHost namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.ExeHost
{
    /// <summary>
    /// Class Program.
    /// </summary>
    class Program
    {
        /// <summary>
        /// Defines the entry point of the application.
        /// </summary>
        /// <param name="args">The arguments.</param>
        static void Main(string[] args)
        {
            ////Uri baseAddress = new Uri("http://127.0.0.1:9998/DataService");
            ////using (ServiceHost host = new ServiceHost(typeof(DataService)))
            ////{
            ////    WebHttpBinding binding = new WebHttpBinding();
            ////    ServiceEndpoint endpoint = host.AddServiceEndpoint(typeof(IDataService), binding, baseAddress);
            ////    WebHttpBehavior httpBehavior = new WebHttpBehavior();
            ////    endpoint.Behaviors.Add(httpBehavior);
            ////    host.Opened += delegate
            ////    {
            ////        Console.WriteLine("Hosted successfully.");
            ////    };
            ////    host.Open();
            ////    Console.ReadLine();
            ////}

            using (ServiceHost host = new ServiceHost(typeof(Service.DataService)))
            {
                host.Opened += Host_Opened;
                host.Faulted += Host_Faulted;
                host.Open();

                Console.ReadLine();
            }
        }

        /// <summary>
        /// Handles the Faulted event of the host control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private static void Host_Faulted(object sender, EventArgs e)
        {
            Console.WriteLine("服务启动失败");
        }

        /// <summary>
        /// Handles the Opened event of the host control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private static void Host_Opened(object sender, EventArgs e)
        {
            Console.WriteLine("服务启动成功");
        }
    }
}
