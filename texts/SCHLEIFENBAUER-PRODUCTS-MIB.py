#
# PySNMP MIB module SCHLEIFENBAUER-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 03:08:46 2024
# On host fv-az736-440 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
schleifenbauerModules, schleifenbauerProducts = mibBuilder.importSymbols("SCHLEIFENBAUER-SMI", "schleifenbauerModules", "schleifenbauerProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, Integer32, TimeTicks, NotificationType, Counter32, Counter64, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "Counter32", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
schleifenbauerProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034, 13, 2))
schleifenbauerProductsMIB.setRevisions(('2015-10-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: schleifenbauerProductsMIB.setRevisionsDescriptions(('The initial revision of this MIB module',))
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setOrganization('Schleifenbauer Engineering')
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setContactInfo('Schleifenbauer Engineering\n         Alain Schuermans\n         Chief Technology Officer\n         Turnhoutseweg 22\n         5541 NX Reusel\n         The Netherlands\n         t. +31 73 5230256\n         f. +31 73 5212383\n         alain@schleifenbauer.eu\n         www.schleifenbauer.eu')
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setDescription('TODO: description.\n        \n         Copyright (c) 2015 by Schleifenbauer Products BV\n        ')
hpdu = MibIdentifier((1, 3, 6, 1, 4, 1, 31034, 11, 1))
dpm3 = MibIdentifier((1, 3, 6, 1, 4, 1, 31034, 11, 2))
mibBuilder.exportSymbols("SCHLEIFENBAUER-PRODUCTS-MIB", dpm3=dpm3, schleifenbauerProductsMIB=schleifenbauerProductsMIB, hpdu=hpdu, PYSNMP_MODULE_ID=schleifenbauerProductsMIB)
