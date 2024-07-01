#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 10:55:02 2024
# On host fv-az665-510 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, Counter32, NotificationType, Gauge32, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "Gauge32", "enterprises", "Counter64")
DisplayString, TextualConvention, TestAndIncr, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TestAndIncr", "AutonomousType")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmManagement.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmManagement.setContactInfo('Postal:     Stuttgarter Str. 45-51\r\n                     72654 Neckartenzlingen\r\n                     Germany\r\n         Phone:      +49 7127 140\r\n         E-mail:     hac.support@belden.com')
if mibBuilder.loadTexts: hmManagement.setDescription('The Hirschmann Private SNMP extension MIB.\r\n\t\t   Copyright (C) 2010. All Rights Reserved.')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hirschmann=hirschmann, PYSNMP_MODULE_ID=hmManagement, hmManagement=hmManagement)
