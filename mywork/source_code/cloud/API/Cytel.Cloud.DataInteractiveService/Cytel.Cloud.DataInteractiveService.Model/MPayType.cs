// ***********************************************************************
// Assembly         : Cytel.Cloud.DataInteractiveService.Model
// Author           : jack
// Created          : 07-14-2016
//
// Last Modified By : jack
// Last Modified On : 07-14-2016
// ***********************************************************************
// <copyright file="MPayType.cs" company="Cytel">
//     Copyright (c) Cytel. All rights reserved.
// </copyright>
// <summary>MPayType<summary>
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
    /// Enum MPayType
    /// </summary>
    public enum MPayType
    {
        /// <summary>
        /// The unknown
        /// </summary>
        Unknown,

        /// <summary>
        /// The cash
        /// </summary>
        Cash,

        /// <summary>
        /// The trafic card
        /// </summary>
        TraficCard,

        /// <summary>
        /// The bank card
        /// </summary>
        BankCard,

        /// <summary>
        /// The mobil
        /// </summary>
        Mobil
    }
}
