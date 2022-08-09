#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.8 at Tue Aug  9 15:48:19 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter32, MibIdentifier, ObjectIdentity, TimeTicks, enterprises, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "enterprises", "Bits", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafeeGATEWAY=mcafeeGATEWAY, mcafee=mcafee, PYSNMP_MODULE_ID=mcafee)
