#
# PySNMP MIB module LANTRONIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lantronix/LANTRONIX-MIB.mib
# Produced by pysmi-1.1.8 at Fri Jul  8 08:58:21 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ObjectIdentity, Integer32, Gauge32, MibIdentifier, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, IpAddress, Unsigned32, NotificationType, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Integer32", "Gauge32", "MibIdentifier", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lantronix = ModuleIdentity((1, 3, 6, 1, 4, 1, 244))
lantronix.setRevisions(('2007-03-01 00:00', '2006-11-10 00:00', '2004-12-13 00:00',))
if mibBuilder.loadTexts: lantronix.setLastUpdated('200703010000Z')
if mibBuilder.loadTexts: lantronix.setOrganization('Lantronix, Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1))
slc = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 1))
slk = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 8))
slp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 9))
slm = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 10))
sls = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 1, 11))
ltxlna = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 10))
ltxlrp = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 11))
ltxlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 244, 12))
mibBuilder.exportSymbols("LANTRONIX-MIB", ltxlna=ltxlna, ltxlrp=ltxlrp, slp=slp, lantronix=lantronix, slc=slc, sls=sls, PYSNMP_MODULE_ID=lantronix, slm=slm, ltxlsw=ltxlsw, products=products, slk=slk)
