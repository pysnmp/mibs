#
# PySNMP MIB module SCHLEIFENBAUER-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 10:59:09 2024
# On host fv-az665-510 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
schleifenbauerProducts, schleifenbauerModules = mibBuilder.importSymbols("SCHLEIFENBAUER-SMI", "schleifenbauerProducts", "schleifenbauerModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, iso, MibIdentifier, Integer32, Counter32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Unsigned32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "iso", "MibIdentifier", "Integer32", "Counter32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Unsigned32", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SCHLEIFENBAUER-PRODUCTS-MIB", schleifenbauerProductsMIB=schleifenbauerProductsMIB, dpm3=dpm3, hpdu=hpdu, PYSNMP_MODULE_ID=schleifenbauerProductsMIB)
