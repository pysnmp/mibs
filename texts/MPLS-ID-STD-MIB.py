#
# PySNMP MIB module MPLS-ID-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-ID-STD-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:08:07 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
MplsGlobalId, MplsCcId, MplsNodeId, MplsIccId = mibBuilder.importSymbols("MPLS-TC-EXT-STD-MIB", "MplsGlobalId", "MplsCcId", "MplsNodeId", "MplsIccId")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Gauge32, TimeTicks, Bits, MibIdentifier, Integer32, Counter32, IpAddress, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "TimeTicks", "Bits", "MibIdentifier", "Integer32", "Counter32", "IpAddress", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 18))
mplsIdStdMIB.setRevisions(('2015-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsIdStdMIB.setRevisionsDescriptions(('This MIB modules defines the MIB objects for MPLS-TP\n        identifiers',))
if mibBuilder.loadTexts: mplsIdStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsIdStdMIB.setContactInfo('\n            Venkatesan Mahalingam\n            Dell Inc,\n            5450 Great America Parkway,\n            Santa Clara, CA 95054, USA\n      Email: venkat.mahalingams@gmail.com\n\n            Kannan KV Sampath\n            Redeem,\n            India\n      Email: kannankvs@gmail.com\n\n            Sam Aldrin\n            Huawei Technologies\n            2330 Central Express Way,\n            Santa Clara, CA 95051, USA\n      Email:  aldrin.ietf@gmail.com\n\n            Thomas D. Nadeau\n      Email: tnadeau@lucidvision.com\n    ')
if mibBuilder.loadTexts: mplsIdStdMIB.setDescription("This MIB module contains identifier object definitions for\n       MPLS Traffic Engineering in transport networks.\n\n       Copyright (c) 2015 IETF Trust and the persons identified as\n       authors of the code.  All rights reserved.\n\n       Redistribution and use in source and binary forms, with or\n       without modification, is permitted pursuant to, and subject to\n       the license terms contained in, the Simplified BSD License set\n       forth in Section 4.c of the IETF Trust's Legal Provisions\n       Relating to IETF Documents\n       (http://trustee.ietf.org/license-info).")
mplsIdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 0))
mplsIdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 1))
mplsIdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2))
mplsIdGlobalId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 1), MplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdGlobalId.setStatus('current')
if mibBuilder.loadTexts: mplsIdGlobalId.setDescription('This object allows the operator or service provider to\n          assign a unique operator identifier, also called the MPLS-TP\n          Global_ID.\n          If this value is used in mplsTunnelExtNodeConfigGlobalId\n          for mapping Global_ID::Node_ID with the local identifier,\n          then this object value MUST NOT be changed.')
mplsIdNodeId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 2), MplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdNodeId.setStatus('current')
if mibBuilder.loadTexts: mplsIdNodeId.setDescription('This object allows the operator or service provider to\n         assign a unique MPLS-TP Node_ID.  The Node_ID is assigned\n         within the scope of the Global_ID/ICC_Operator_ID.\n         If this value is used in mplsTunnelExtNodeConfigNodeId\n         for mapping Global_ID::Node_ID with the local identifier,\n         then this object value SHOULD NOT be changed.\n         If this value is used in mplsTunnelExtNodeConfigNodeId\n         for mapping ICC_Operator_ID::Node_ID with the local\n         identifier, then this object value MUST NOT be changed.')
mplsIdCc = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 3), MplsCcId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdCc.setReference('MPLS-TP Identifiers Following ITU-T Conventions,\n          RFC 6923, Section 3')
if mibBuilder.loadTexts: mplsIdCc.setStatus('current')
if mibBuilder.loadTexts: mplsIdCc.setDescription('This object allows the operator or service provider to\n         assign a Country Code (CC) to the node.  Global\n         uniqueness of ICC is assured by concatenating the ICC\n         with a Country Code (CC).\n         If this value is used in mplsTunnelExtNodeConfigCcId\n         for mapping ICC_Operator_ID::Node_ID with the local\n         identifier, then this object value MUST NOT be changed.')
mplsIdIcc = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 4), MplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdIcc.setReference('MPLS-TP Identifiers Following ITU-T Conventions,\n          RFC 6923, Section 3')
if mibBuilder.loadTexts: mplsIdIcc.setStatus('current')
if mibBuilder.loadTexts: mplsIdIcc.setDescription('This object allows the operator or service provider to\n         assign a unique MPLS-TP ITU-T Carrier Code (ICC) to\n         the node.  Together, the CC and the ICC form\n         the ICC_Operator_ID as CC::ICC.\n         If this value is used in mplsTunnelExtNodeConfigIccId\n         for mapping ICC_Operator_ID::Node_ID with the local\n         identifier, then this object value MUST NOT be changed.')
mplsIdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1))
mplsIdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2))
mplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 1)).setObjects(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"), ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdModuleFullCompliance = mplsIdModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsIdModuleFullCompliance.setDescription('Compliance statement for agents that provide full\n          support of the MPLS-ID-STD-MIB module.')
mplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 2)).setObjects(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"), ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdModuleReadOnlyCompliance = mplsIdModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsIdModuleReadOnlyCompliance.setDescription('Compliance statement for agents that only provide\n               read-only support for the MPLS-ID-STD-MIB module.')
mplsIdIpOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 1)).setObjects(("MPLS-ID-STD-MIB", "mplsIdGlobalId"), ("MPLS-ID-STD-MIB", "mplsIdNodeId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdIpOperatorGroup = mplsIdIpOperatorGroup.setStatus('current')
if mibBuilder.loadTexts: mplsIdIpOperatorGroup.setDescription('The objects in this group are optional for an\n                 ICC-based node.')
mplsIdIccOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 2)).setObjects(("MPLS-ID-STD-MIB", "mplsIdNodeId"), ("MPLS-ID-STD-MIB", "mplsIdCc"), ("MPLS-ID-STD-MIB", "mplsIdIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdIccOperatorGroup = mplsIdIccOperatorGroup.setStatus('current')
if mibBuilder.loadTexts: mplsIdIccOperatorGroup.setDescription('The objects in this group are optional for an\n                IP-based node.')
mibBuilder.exportSymbols("MPLS-ID-STD-MIB", mplsIdModuleFullCompliance=mplsIdModuleFullCompliance, mplsIdCompliances=mplsIdCompliances, PYSNMP_MODULE_ID=mplsIdStdMIB, mplsIdIpOperatorGroup=mplsIdIpOperatorGroup, mplsIdIccOperatorGroup=mplsIdIccOperatorGroup, mplsIdIcc=mplsIdIcc, mplsIdConformance=mplsIdConformance, mplsIdObjects=mplsIdObjects, mplsIdModuleReadOnlyCompliance=mplsIdModuleReadOnlyCompliance, mplsIdNotifications=mplsIdNotifications, mplsIdNodeId=mplsIdNodeId, mplsIdGlobalId=mplsIdGlobalId, mplsIdStdMIB=mplsIdStdMIB, mplsIdCc=mplsIdCc, mplsIdGroups=mplsIdGroups)
