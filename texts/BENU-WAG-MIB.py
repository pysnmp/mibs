#
# PySNMP MIB module BENU-WAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-WAG-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 11:12:29 2024
# On host fv-az525-771 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
benuPlatSerMIB, = mibBuilder.importSymbols("BENU-PLATFORM-SERVICE-MIB", "benuPlatSerMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, TimeTicks, iso, ModuleIdentity, Gauge32, ObjectIdentity, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "TimeTicks", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuWAG = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1))
benuWAG.setRevisions(('2012-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuWAG.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuWAG.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: benuWAG.setOrganization('Benu Networks')
if mibBuilder.loadTexts: benuWAG.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: benuWAG.setDescription('The MIB module for defining all mib sub modules \n        that are specific to WiFiAccessGateway\n        Copyright (C) 2001, 2008 by Benu Networks, Inc.\n        All rights reserved.')
mibBuilder.exportSymbols("BENU-WAG-MIB", PYSNMP_MODULE_ID=benuWAG, benuWAG=benuWAG)
