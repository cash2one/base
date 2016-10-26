// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MExitRequest.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MExitRequest<summary>
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
    /// Class MExitRequest.
    /// </summary>
    public class MExitRequest
    {
        /// <summary>
        /// Gets or sets the park unique identifier.
        /// </summary>
        /// <value>The park unique identifier.</value>
        public string ParkId { get; set; }

        /// <summary>
        /// Gets or sets the name of the gate.
        /// </summary>
        /// <value>The name of the gate.</value>
        public string GateName { get; set; }

        /// <summary>
        /// Gets or sets the backup time.
        /// </summary>
        /// <value>The backup time.</value>
        public DateTime KTime { get; set; }

        /// <summary>
        /// Gets or sets the type of the backup.
        /// </summary>
        /// <value>The type of the backup.</value>
        public MCarType KType { get; set; }

        /// <summary>
        /// Gets or sets the space information.
        /// </summary>
        /// <value>The space information.</value>
        public MSpaceInfo SpaceInfo { get; set; }

        /// <summary>
        /// Gets or sets the card no.
        /// </summary>
        /// <value>The card no.</value>
        public string CardNo { get; set; }

        /// <summary>
        /// Gets or sets the plate no.
        /// </summary>
        /// <value>The plate no.</value>
        public string PlateNo { get; set; }

        /// <summary>
        /// 停车时长(单位：秒).
        /// </summary>
        /// <value>The length of the park.</value>
        public string ParkLength { get; set; }

        /// <summary>
        /// 收费金额(单位：分).
        /// </summary>
        /// <value>The charge.</value>
        public string Charge { get; set; }

        /// <summary>
        /// Gets or sets the type of the pay.
        /// </summary>
        /// <value>The type of the pay.</value>
        public MPayType PayType { get; set; }
    }
}
