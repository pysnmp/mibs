#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.12 at Fri Jul 19 10:07:46 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter64, iso, Integer32, NotificationType, ModuleIdentity, IpAddress, Counter32, Unsigned32, MibIdentifier, Gauge32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "iso", "Integer32", "NotificationType", "ModuleIdentity", "IpAddress", "Counter32", "Unsigned32", "MibIdentifier", "Gauge32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafee=mcafee, PYSNMP_MODULE_ID=mcafee, mcafeeGATEWAY=mcafeeGATEWAY)
