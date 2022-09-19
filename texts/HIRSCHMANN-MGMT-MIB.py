#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 07:28:49 2022
# On host fv-az215-626 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Unsigned32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, Bits, Counter32, NotificationType, TimeTicks, ModuleIdentity, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Unsigned32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "Bits", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "Counter64")
TestAndIncr, DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "DisplayString", "TextualConvention", "AutonomousType")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmManagement.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmManagement.setContactInfo('Postal:     Stuttgarter Str. 45-51\r\n                     72654 Neckartenzlingen\r\n                     Germany\r\n         Phone:      +49 7127 140\r\n         E-mail:     hac.support@belden.com')
if mibBuilder.loadTexts: hmManagement.setDescription('The Hirschmann Private SNMP extension MIB.\r\n\t\t   Copyright (C) 2010. All Rights Reserved.')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hirschmann=hirschmann, hmManagement=hmManagement, PYSNMP_MODULE_ID=hmManagement)
