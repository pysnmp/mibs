#
# PySNMP MIB module COLUBRIS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SMI.my
# Produced by pysmi-1.1.12 at Mon Oct 28 02:10:29 2024
# On host fv-az1014-591 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, enterprises, NotificationType, Unsigned32, ModuleIdentity, Counter32, Counter64, IpAddress, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "enterprises", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubris = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744))
if mibBuilder.loadTexts: colubris.setLastUpdated('200402100000Z')
if mibBuilder.loadTexts: colubris.setOrganization('Colubris Networks, Inc.')
colubrisProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 1))
if mibBuilder.loadTexts: colubrisProducts.setStatus('current')
colubrisMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 2))
if mibBuilder.loadTexts: colubrisMgmt.setStatus('deprecated')
colubrisExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 3))
if mibBuilder.loadTexts: colubrisExperiment.setStatus('current')
colubrisModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 4))
if mibBuilder.loadTexts: colubrisModules.setStatus('current')
colubrisMgmtV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 5))
if mibBuilder.loadTexts: colubrisMgmtV2.setStatus('current')
extensions = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 6))
if mibBuilder.loadTexts: extensions.setStatus('current')
variation = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 7))
if mibBuilder.loadTexts: variation.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SMI", extensions=extensions, colubrisProducts=colubrisProducts, variation=variation, colubrisMgmt=colubrisMgmt, PYSNMP_MODULE_ID=colubris, colubrisModules=colubrisModules, colubrisExperiment=colubrisExperiment, colubris=colubris, colubrisMgmtV2=colubrisMgmtV2)
