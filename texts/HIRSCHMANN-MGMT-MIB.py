#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:27:40 2024
# On host fv-az1986-495 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Counter32, IpAddress, Integer32, TimeTicks, Bits, NotificationType, ObjectIdentity, iso, enterprises, MibIdentifier, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Counter32", "IpAddress", "Integer32", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity", "iso", "enterprises", "MibIdentifier", "Counter64", "Gauge32")
TestAndIncr, AutonomousType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "AutonomousType", "DisplayString", "TextualConvention")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmManagement.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmManagement.setContactInfo('Postal:     Stuttgarter Str. 45-51\r\n                     72654 Neckartenzlingen\r\n                     Germany\r\n         Phone:      +49 7127 140\r\n         E-mail:     hac.support@belden.com')
if mibBuilder.loadTexts: hmManagement.setDescription('The Hirschmann Private SNMP extension MIB.\r\n\t\t   Copyright (C) 2010. All Rights Reserved.')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hmManagement=hmManagement, hirschmann=hirschmann, PYSNMP_MODULE_ID=hmManagement)
