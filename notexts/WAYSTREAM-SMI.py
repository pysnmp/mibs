#
# PySNMP MIB module WAYSTREAM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-SMI
# Produced by pysmi-1.1.12 at Tue Dec  3 10:12:15 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, Counter32, enterprises, IpAddress, MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Bits, ModuleIdentity, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Counter32", "enterprises", "IpAddress", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "ModuleIdentity", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
waystream = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303))
waystream.setRevisions(('2017-02-10 11:00', '2011-01-11 18:01', '2009-03-23 10:39', '2008-01-17 14:05', '2007-05-11 12:28',))
if mibBuilder.loadTexts: waystream.setLastUpdated('201702101100Z')
if mibBuilder.loadTexts: waystream.setOrganization('Waystream AB')
wsProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1))
if mibBuilder.loadTexts: wsProduct.setStatus('current')
wsConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2))
if mibBuilder.loadTexts: wsConfig.setStatus('current')
ipdConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2, 1))
if mibBuilder.loadTexts: ipdConfig.setStatus('current')
wsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 3))
if mibBuilder.loadTexts: wsExperiment.setStatus('current')
wsMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 4))
if mibBuilder.loadTexts: wsMgmt.setStatus('current')
wsModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 5))
if mibBuilder.loadTexts: wsModules.setStatus('current')
pfSW = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 6))
if mibBuilder.loadTexts: pfSW.setStatus('current')
mibBuilder.exportSymbols("WAYSTREAM-SMI", PYSNMP_MODULE_ID=waystream, ipdConfig=ipdConfig, wsModules=wsModules, wsExperiment=wsExperiment, wsConfig=wsConfig, wsProduct=wsProduct, waystream=waystream, pfSW=pfSW, wsMgmt=wsMgmt)
