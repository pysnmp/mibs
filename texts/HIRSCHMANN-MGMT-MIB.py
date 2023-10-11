#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.8 at Wed Oct 11 11:28:52 2023
# On host fv-az456-991 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, TimeTicks, Unsigned32, Bits, enterprises, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "Unsigned32", "Bits", "enterprises", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Counter32", "Integer32")
DisplayString, TextualConvention, AutonomousType, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType", "TestAndIncr")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmManagement.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmManagement.setContactInfo('Postal:     Stuttgarter Str. 45-51\r\n                     72654 Neckartenzlingen\r\n                     Germany\r\n         Phone:      +49 7127 140\r\n         E-mail:     hac.support@belden.com')
if mibBuilder.loadTexts: hmManagement.setDescription('The Hirschmann Private SNMP extension MIB.\r\n\t\t   Copyright (C) 2010. All Rights Reserved.')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", PYSNMP_MODULE_ID=hmManagement, hmManagement=hmManagement, hirschmann=hirschmann)
