#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 08:55:42 2024
# On host fv-az1149-759 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, Counter64, NotificationType, ModuleIdentity, Gauge32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, iso, ObjectIdentity, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "iso", "ObjectIdentity", "Integer32", "enterprises")
TextualConvention, AutonomousType, TestAndIncr, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "TestAndIncr", "DisplayString")
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
