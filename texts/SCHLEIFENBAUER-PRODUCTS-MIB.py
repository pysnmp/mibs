#
# PySNMP MIB module SCHLEIFENBAUER-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:32:02 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
schleifenbauerModules, schleifenbauerProducts = mibBuilder.importSymbols("SCHLEIFENBAUER-SMI", "schleifenbauerModules", "schleifenbauerProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Gauge32, MibIdentifier, Counter64, ObjectIdentity, iso, Bits, ModuleIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Gauge32", "MibIdentifier", "Counter64", "ObjectIdentity", "iso", "Bits", "ModuleIdentity", "Integer32", "IpAddress")
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
mibBuilder.exportSymbols("SCHLEIFENBAUER-PRODUCTS-MIB", dpm3=dpm3, PYSNMP_MODULE_ID=schleifenbauerProductsMIB, hpdu=hpdu, schleifenbauerProductsMIB=schleifenbauerProductsMIB)
