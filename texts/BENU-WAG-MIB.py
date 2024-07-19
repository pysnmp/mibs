#
# PySNMP MIB module BENU-WAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-WAG-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 09:59:37 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
benuPlatSerMIB, = mibBuilder.importSymbols("BENU-PLATFORM-SERVICE-MIB", "benuPlatSerMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, Unsigned32, Integer32, ObjectIdentity, iso, MibIdentifier, Gauge32, TimeTicks, Bits, Counter32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "MibIdentifier", "Gauge32", "TimeTicks", "Bits", "Counter32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuWAG = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1))
benuWAG.setRevisions(('2012-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuWAG.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuWAG.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: benuWAG.setOrganization('Benu Networks')
if mibBuilder.loadTexts: benuWAG.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: benuWAG.setDescription('The MIB module for defining all mib sub modules \n        that are specific to WiFiAccessGateway\n        Copyright (C) 2001, 2008 by Benu Networks, Inc.\n        All rights reserved.')
mibBuilder.exportSymbols("BENU-WAG-MIB", benuWAG=benuWAG, PYSNMP_MODULE_ID=benuWAG)
