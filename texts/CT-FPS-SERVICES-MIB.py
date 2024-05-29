#
# PySNMP MIB module CT-FPS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FPS-SERVICES-MIB
# Produced by pysmi-1.1.12 at Wed May 29 02:43:18 2024
# On host fv-az569-426 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ctFPSServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFPSServices")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, Counter32, TimeTicks, Unsigned32, iso, ModuleIdentity, MibIdentifier, Gauge32, Integer32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Counter32", "TimeTicks", "Unsigned32", "iso", "ModuleIdentity", "MibIdentifier", "Gauge32", "Integer32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFPSActivity = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1))
ctLookUpFwdActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctLookUpFwdActivity.setStatus('mandatory')
if mibBuilder.loadTexts: ctLookUpFwdActivity.setDescription('')
ctINBActivity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctINBActivity.setStatus('mandatory')
if mibBuilder.loadTexts: ctINBActivity.setDescription('')
mibBuilder.exportSymbols("CT-FPS-SERVICES-MIB", ctFPSActivity=ctFPSActivity, ctLookUpFwdActivity=ctLookUpFwdActivity, ctINBActivity=ctINBActivity)
