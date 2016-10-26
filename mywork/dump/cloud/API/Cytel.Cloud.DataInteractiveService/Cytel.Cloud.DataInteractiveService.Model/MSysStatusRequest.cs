// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MSysStatusRequest.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MSysStatusRequest<summary>
// ***********************************************************************
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

/// <summary>
/// The Model namespace.
/// </summary>
namespace Cytel.Cloud.DataInteractiveService.Model
{
    /// <summary>
    /// Class MSysStatusRequest.
    /// </summary>
    public class MSysStatusRequest
    {
        /// <summary>
        /// Gets or sets the park unique identifier.
        /// </summary>
        /// <value>The park unique identifier.</value>
        public string ParkId { get; set; }

        /// <summary>
        /// Gets or sets the status.
        /// </summary>
        /// <value>The status.</value>
        public MSystemStatus Status { get; set; }

        /// <summary>
        /// Gets or sets the type of the alarm.
        /// </summary>
        /// <value>The type of the alarm.</value>
        public MAlarmType AlarmType { get; set; }
    }
}
