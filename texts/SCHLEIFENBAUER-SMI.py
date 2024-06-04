#
# PySNMP MIB module SCHLEIFENBAUER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-SMI
# Produced by pysmi-1.1.12 at Tue Jun  4 02:45:03 2024
# On host fv-az1200-411 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Counter32, TimeTicks, Counter64, Gauge32, enterprises, Bits, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Counter32", "TimeTicks", "Counter64", "Gauge32", "enterprises", "Bits", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
schleifenbauer = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034))
schleifenbauer.setRevisions(('2015-10-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: schleifenbauer.setRevisionsDescriptions(('The initial revision of this MIB module',))
if mibBuilder.loadTexts: schleifenbauer.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauer.setOrganization('Schleifenbauer Engineering')
if mibBuilder.loadTexts: schleifenbauer.setContactInfo('Schleifenbauer Engineering\n         Alain Schuermans\n         Chief Technology Officer\n         Rietwaard 15\n         5236 WC ‘s-Hertogenbosch\n         The Netherlands\n         t +31 (0)73 52 30256\n         f +31 (0)73 521 23 83\n         alain@schleifenbauer.eu\n         www.schleifenbauer.eu')
if mibBuilder.loadTexts: schleifenbauer.setDescription('The Structure of Management Information for the Schleifenbauer\n         enterprise.\n        \n         Copyright (c) 2015 by Schleifenbauer Products BV')
schleifenbauerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 11))
if mibBuilder.loadTexts: schleifenbauerProducts.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerProducts.setDescription('schleifenbauerProducts is the root OBJECT IDENTIFIER from which\n         sysObjectId values are assigned. Acutal values are defined in \n         SCHLEIFENBAUER-PRODUCTS-MIB.')
schleifenbauerMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 12))
if mibBuilder.loadTexts: schleifenbauerMgmt.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerMgmt.setDescription('schleifenbauerMgmt is the main subtree for new mib development.')
schleifenbauerModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 13))
if mibBuilder.loadTexts: schleifenbauerModules.setStatus('current')
if mibBuilder.loadTexts: schleifenbauerModules.setDescription('schleifenbauerModules provides a root object identifier from which\n         MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("SCHLEIFENBAUER-SMI", schleifenbauerModules=schleifenbauerModules, schleifenbauerMgmt=schleifenbauerMgmt, schleifenbauerProducts=schleifenbauerProducts, PYSNMP_MODULE_ID=schleifenbauer, schleifenbauer=schleifenbauer)
