#
# PySNMP MIB module LANTRONIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/lantronix/LANTRONIX-MIB.mib
# Produced by pysmi-1.1.8 at Thu Apr 27 09:21:02 2023
# On host fv-az247-870 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, Counter32, Bits, ModuleIdentity, Unsigned32, Gauge32, TimeTicks, iso, Integer32, Counter64, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Counter32", "Bits", "ModuleIdentity", "Unsigned32", "Gauge32", "TimeTicks", "iso", "Integer32", "Counter64", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LANTRONIX-MIB", lantronix=lantronix, products=products, ltxlrp=ltxlrp, slk=slk, ltxlsw=ltxlsw, slm=slm, slc=slc, PYSNMP_MODULE_ID=lantronix, slp=slp, ltxlna=ltxlna, sls=sls)
